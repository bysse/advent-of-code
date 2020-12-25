%define SYS_READ        0
%define SYS_WRITE       1
%define SYS_OPEN        2
%define SYS_CLOSE       3
%define SYS_STAT        4
%define SYS_MMAP        9
%define SYS_MUNMAP      11

%define O_RDONLY		0

%define PROT_READ       4
%define PROT_WRITE      2

%define MAP_PRIVATE     0x02
%define MAP_ANONYMOUS   0x20


struc STAT        
    .st_dev         resq 1
    .st_ino         resq 1
    .st_nlink       resq 1
    .st_mode        resd 1
    .st_uid         resd 1
    .st_gid         resd 1
    .pad0           resb 4
    .st_rdev        resq 1
    .st_size        resq 1
    .st_blksize     resq 2
    .st_time        resq 6
endstruc

SECTION .data

filebuffer:     dq  0,0,0,0,0,0,0,0

SECTION .bss

%define sizeof(x) x %+ _size
stat_buffer:    db	sizeof(STAT)

SECTION .text

; filename in rdi
load_file: 
        ; get size of file                        
        push    rbp 
        push    rdi
        push    rdi                     ; store filename on the stack twice
        
        mov     rax, SYS_STAT           ; stat the file
        pop     rdi
        mov     rsi, stat_buffer
        syscall
               
        cmp     rax, 0
        jnz     load_file_error

        ; allocate memory file size

        mov     rdi, [stat_buffer + STAT.st_size]
        call    allocate
        mov     [filebuffer], rax

        ; open file
        mov     rax, SYS_OPEN
        pop     rdi
        mov     rsi, O_RDONLY
        mov     rdx, 0                  ; mode = 0
        syscall

        cmp     rax, 0
        jle     load_file_error
        mov     r8, rax                 ; store file descriptor

        ; read from file
        mov     rax, SYS_READ
        mov     rdi, r8
        mov     rsi, [filebuffer]
        mov     rdx, [stat_buffer + STAT.st_size]
        syscall

        ; close the file
        mov     rax, SYS_CLOSE
        mov     rdi, r8
        syscall

        cmp     rax, 0
        jnz     load_file_error

        ; prepare the return value
        mov     rax, [stat_buffer + STAT.st_size]

        pop     rbp
        ret

load_file_error:

        ; prepare the return value
        xor     rax, rax

        pop     rbp
        ret


; allocate memory - size in rdi
allocate:
        push    r11
        push    r10
        push    r9
        push    r8
        push    rdx
        push    rcx

        mov     rax,    SYS_MMAP
        mov     rsi,    rdi
        mov     rdi,    0                   ; addr = NULL
        mov     rdx,    PROT_READ | PROT_WRITE
        mov     r10,    MAP_PRIVATE | MAP_ANONYMOUS
        mov     r8,     -1
        mov     r9,     0
        syscall

        pop     rcx
        pop     rdx
        pop     r8
        pop     r9
        pop     r10
        pop     r11

        ret

; deallocate memory - rdi (addr), rdi (length)
de_allocate:
        mov     rax,    SYS_MUNMAP
        syscall
        ret

; convert a string to number - rdi (string)
to_int:
        mov     rax, 1          ; power
        mov     r8, 0           ; length
        mov     r10, 0          ; result
        mov     rsi, rdi        ; string
ti_length_loop:
        mov     rbx, [rsi]
        cmp     bl, 0
        jz      ti_calc_loop
        imul    rax, rax, 10
        inc     rsi
        inc     r8
        jmp     ti_length_loop
        
ti_calc_loop:
        mov     rbx, [rdi]
        cmp     bl, 0           ; check exit condition
        jz      ti_calc_exit

        mov     rcx, 10         ; power /= 10
        xor     rdx, rdx        
        idiv    rcx

        xor     rdx, rdx
        mov     dl, bl
        sub     rdx, 48         ; digit - '0'
        imul    rdx, rax        ; *= power
        
        add     r10, rdx        ; add to result
        inc     rdi             ; next character

        dec     r8
        jnz     ti_calc_loop
ti_calc_exit:
        mov     rax, r10
        ret


; convert a number to a string - rdi (number)
output_number:
        mov     r8, 2           ; length, 2 because of \n and the null termination
        mov     r9, rdi         ; number
        mov     r10, 1          ; power        
        mov     r11, 0          ; negative

        cmp     rdi, 0
        jge     on_length_loop

        neg     rdi             ; invert the number to a positive one
        mov     r11, 1          ; indicate that the number is negative

on_length_loop:
        cmp     r10, rdi
        jge     on_length_exit    
        imul    r10, r10, 10
        inc     r8
        jmp     on_length_loop
on_length_exit:
        add     r8, r11         ; adjust length for - sign        

        ; allocate memory for the string
        mov     rdi, r8
        call    allocate
        mov     r12, rax        ; start of memory in r12
        mov     rsi, rax        ; current char in rsi

        ; adjust the power
        mov     rax, r10
        mov     rcx, 10         ; power /= 10
        xor     rdx, rdx        
        idiv    rcx
        mov     r10, rax

        ; add the minus sign
        cmp     r11, 0
        jz      on_positive_number
        mov     [rsi], byte 45  ; '-'
        inc     rsi        
on_positive_number:        
        
        mov     rax, r9         ; number
        mov     rdi, r8         ; length
        sub     rdi, 2

on_fill_buffer_loop:
        ; divide the number by power
        mov     rcx, r10
        xor     rdx, rdx        
        cmp     rax, 0
        jz      on_zero

        idiv    rcx            

on_zero:        
        mov     r14, rdx        ; reminder        
        
        add     al, 48          ; '0' + div
        mov     [rsi], byte al  ; write the character

        ; lower the power
        mov     rax, r10
        mov     rcx, 10         ; power /= 10
        xor     rdx, rdx        
        idiv    rcx
        mov     r10, rax        

        ; exit condition
        mov     rax, r14        ; use the reminder for the next loop 
        inc     rsi             ; next char
        dec     rdi
        jnz     on_fill_buffer_loop
        
        mov     [rsi], word 0x000a  ; add new line and null termination

on_print:        
        ; print the buffer
        mov     rax, SYS_WRITE
        mov     rdi, 1          ; stdout
        mov     rsi, r12
        mov     rdx, r8
        syscall

        ; deallocate the buffer
        mov     rdi, r12
        mov     rsi, r8
        call    de_allocate

        ret
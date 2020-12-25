DEFAULT REL

global _start

SECTION .data
filename:
                        db  "../input/input1.txt", 0h

SECTION .bss

numbers:                dq 0,0,0,0,0,0,0,0
lines:                  dq 0,0,0,0,0,0,0,0
filebuffer_size:        dw 0,0,0,0
numberbuffer_size:      dw 0,0,0,0
result_a:               dw 0,0,0,0
result_b:               dw 0,0,0,0

SECTION .text
_start: 
        push    rbp

        ; load the input
        mov     rdi, filename
        call    load_file        
        cmp     rax, 0                  ; exit if bytes read is 0
        jz      exit
        mov     [filebuffer_size], eax  ; store the number of bytes allocated
        
        ; count how many lines the file has
        mov     rax, [filebuffer]
        mov     rcx, 0
size_loop:
        mov     rbx, [rax]
        cmp     bl, 10
        jnz     size_loop_skip
        inc     rcx
size_loop_skip:
        inc     rax
        dec     rdx
        ja      size_loop
        mov     [lines], rcx             ; number of lines

        ; allocate memory for 64 bit numbers
        imul    rdi, rcx, 8
        mov     [numberbuffer_size], edi; store the number of bytes allocated                
        call    allocate
        mov     [numbers], rax        

        ; parse the numbers
        mov     r12, [filebuffer]       ; current char
        mov     rcx, [lines]            ; number of lines
        mov     rdx, [numbers]          ; destination buffer
        mov     rdi, r12                ; start of current number
        dec     r12
parse_loop:                             ; find the end of line
        inc     r12
        mov     rbx, [r12]
        cmp     bl, 10
        jnz     parse_loop
        
        mov     [r12], byte 0           ; write EOL

        cmp     rdi, rdx
        jz      skip_parsing

        ; parse the string to a number
        push    rdx
        push    rcx
        call    to_int
        pop     rcx
        pop     rdx

        ; store the number in memory
        mov     [rdx], rax
        add     rdx, 8

skip_parsing:        
        inc     r12                     ; move to the next char           
        mov     rdi, r12                ; store the start of the number

        dec     rcx
        ja      parse_loop              

        ; calculate numbers

        xor     rax, rax
        mov     [result_a], rax
        mov     [result_b], rax

        mov     r10, [lines]            ; i
        mov     r11, [lines]            ; j

        dec     r10
        dec     r11

part_a_loop:
        dec     r11     

        ; calculate part a
        mov     rdx, [numbers]          ; source buffer
        lea     rcx, [rdx + 8*r10]      ; load next address for i
        lea     rdx, [rdx + 8*r11]      ; load next address for j
        mov     rax, [rcx]
        mov     rbx, [rdx]
        mov     rcx, rax                ; copy of number[i]

        add     rax, rbx                ; sum the numbers
        cmp     rax, 2020
        jne     not_part_a

        imul    rcx, rbx                ; calculate the product
        mov     [result_a], rcx

not_part_a:

        cmp     [result_b], dword 0     ; skip calculation if we already have a result
        jnz     end_of_b

        mov     r15, rax                ; store sum in r11

        ; calculate part b
        mov     r12, [lines]            ; k
        dec     r12

part_b_loop:
        
        lea     r13, [rdx + 8*r12]      ; load address for k
        mov     r14, [r13]              ; k in r14
        
        mov     rax, r14
        add     rax, r15
        cmp     rax, 2020               ; sum and compare

        jne     not_part_b

        mov     rax, r14
        imul    rax, rbx
        imul    rax, rcx
        mov     [result_b], rax         ; calculate the product

not_part_b:
        dec     r12
        jnz     part_b_loop             ; loop while k > 0
end_of_b:        

        cmp     r11, 0
        jnz     part_a_loop             ; loop while j > 0

        dec     r10                     ; decrease i
        mov     r11, r10                ; set j = i
        cmp     r10, 0
        jnz     part_a_loop             ; loop while i > 0

        ; output result A
        mov     rdi, [result_a]
        call    output_number

        ; output result B
        mov     rdi, [result_b]
        call    output_number

        ; free the memory buffers
        xor     rsi, rsi
        mov     rdi, [filebuffer]
        mov     esi, [filebuffer_size]
        call    de_allocate

        mov     rdi, [numbers]
        mov     esi, [numberbuffer_size]
        call    de_allocate

exit:
        pop     rbp

        mov     ebx, 0
        mov     eax, 1
        int     80h                  

%include        'io.asm'    

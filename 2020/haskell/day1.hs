
main = do 
        c <- readFile "../input/input1.txt"
        let ints = map (\x -> read x :: Int) (lines c)
        let a = head [x*y | x <- ints, y <- ints, x+y == 2020]
        let b = head [x*y*z | x <- ints, y <- ints, z <- ints, x+y+z == 2020]
        putStrLn ("A: " ++ show a)
        putStrLn ("B: " ++ show b)
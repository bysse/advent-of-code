import Data.Char (ord)
import Data.List (sort)

main = do
    c <- readFile "../input/input5.txt"
    let seats = sort $ map toNum (lines c)
    putStrLn ("A: " ++ show (last seats))
    putStrLn ("B: " ++ show (sum [head seats .. last seats] - sum seats))
    where
        toNum = foldl (\a x -> 2*a + mod (mod (ord x) 7) 2) 0
import Data.Map (Map, fromList, keys, lookup)
import Data.Maybe (isJust, fromMaybe)
import Data.List (find)

bagId x = foldl1 (\a x -> a ++ "-" ++ x) (take 2 x)

bagList :: [String] -> [(Int, String)]
bagList [] = []
bagList xs 
    | head xs == "no" = []
    | otherwise = (n, id) : bagList (drop 4 xs)
        where 
            n = read (head xs) :: Int
            id = bagId (drop 1 xs)

parse :: [String] -> (String, [(Int, String)])
parse xs = (bagId xs, bagList rest)
    where 
        rest = drop 4 xs
search :: Map String [(Int, String)] -> String -> String -> Bool
search dict target x 
    | target == x = True
    | otherwise   = case Data.Map.lookup x dict of
        Just content -> isJust $ find (search dict target) (map snd content)
        Nothing      -> False

countBags :: Map String [(Int, String)] -> String -> Int
countBags dict x = 1 + sum (map (\x -> fst x * countBags dict (snd x)) bags)
    where
        bags = fromMaybe [] (Data.Map.lookup x dict)

main = do
    c <- readFile "../input/input7.txt"
    let target = "shiny-gold"
    let dict = fromList $ map (parse . words) (lines c)
    let partA = sum [fromEnum (search dict target x) | x <- keys dict, x /= target]
    putStrLn ("A: " ++ show partA)
    let partB = countBags dict target - 1
    putStrLn ("B: " ++ show partB)
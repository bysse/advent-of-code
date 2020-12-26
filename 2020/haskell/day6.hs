import qualified Data.Set as Set

group :: [String] -> [String] -> [[String]]
group [] a = [a]
group (x:xs) a = case length x of
        0 -> a : group xs []
        _ -> group xs (a ++ [x])

main = do
    c <- readFile "../input/input6.txt"
    let groups = group (lines c) []
    let sets = map (map Set.fromList) groups
    let a = sum $ map (Set.size . Set.unions) sets
    putStrLn ("A: " ++ show a)
    let b = sum $ map (Set.size . foldl1 Set.intersection) sets
    putStrLn ("B: " ++ show b)

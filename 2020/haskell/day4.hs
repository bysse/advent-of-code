import Data.Map (Map, fromList)
import Data.Maybe
import Data.List.Split (splitOn)
import Data.List (sort)
import Text.Regex
import Debug.Trace

inRange (low, high) value = low <= value && value <= high

group :: [String] -> [String] -> [[String]]
group [] a = [a]
group (x:xs) a = case length x of
        0 -> a : group xs []
        _ -> group xs (a ++ [x])

hasAll :: [String] -> [String] -> Bool
hasAll xs ys = foldl (\a x -> elem x ys && a) True xs

parse :: [String] -> [(String,String)]
parse xs = map ((\(a:b) -> (a, head b)) . splitOn ":") $ concatMap (splitOn " ") xs

hasAllProperties :: [(String, String)] -> Bool
hasAllProperties xs = hasAll ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] (map fst xs)

isValid :: (String, String) -> Bool
isValid ("byr", value) = inRange (1920, 2002) year where year = read value :: Int
isValid ("iyr", value) = inRange (2010, 2020) year where year = read value :: Int
isValid ("eyr", value) = inRange (2020, 2030) year where year = read value :: Int
isValid ("hgt", value) = case matchRegex (mkRegex "([0-9]+)(in|cm)") value of
                                Just [height, unit] -> inRange interval (read height :: Int) 
                                        where interval = if unit == "cm" then (150, 193) else (59, 76)
                                _ -> False
isValid ("hcl", value) = isJust $ matchRegex (mkRegex "^#[0-9a-f]{6}$") value 
isValid ("ecl", value) = value `elem` ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
isValid ("pid", value) = isJust $ matchRegex (mkRegex "^[0-9]{9}$") value 
isValid ("cid", _) = True
isValid _ = False

showP _ [] = []
showP p (x:xs) = if p == fst x then [x] else showP p xs

main = do 
        c <- readFile "../input/input4.txt"
        let field = lines c
        let passports = map parse (group field [])
        let valid = filter hasAllProperties passports
        putStrLn ("A: " ++ show (length valid))
        putStrLn ("B: " ++ show (length (filter (all isValid) valid)))

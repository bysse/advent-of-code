import Text.Regex

data Rule = Rule Int Int Char deriving (Show) 

inRange low high x = low <= x && x <= high
b2i x = if x then 1 else 0

policyA :: Maybe (Rule, String) -> Bool
policyA (Just (Rule l h ch, pw)) = inRange l h (length $ filter (==ch) pw)
policyA Nothing = False

policyB :: Maybe (Rule, String) -> Bool
policyB (Just (Rule l h ch, pw)) = (pw !! (l-1) == ch) /= (pw !! (h-1) == ch)
policyB Nothing = False
    
parse :: [Char] -> Maybe (Rule, String)
parse x = 
    case matchRegex (mkRegex "([0-9]+)-([0-9]+) (.): (.*)") x of
        Just (l:h:char:pw:_) -> Just (Rule low high (head char), pw)
            where 
                low = read l :: Int
                high = read h :: Int
        _ -> Nothing

main = do 
        c <- readFile "../input/input2.txt"
        let rules = map parse (lines c)
        let a = sum $ map (b2i . policyA) rules
        let b = sum $ map (b2i . policyB) rules
        putStrLn ("A: " ++ show a)
        putStrLn ("B: " ++ show b)

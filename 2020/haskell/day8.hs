import Text.Regex
import Data.Maybe (fromJust)
import Data.Map (Map, fromList, lookup, adjust)

parse x 
    | b == "+"  = (a,  ci)
    | otherwise = (a, -ci)
    where
        [a,b,c] = fromJust (matchRegex (mkRegex "([a-z]+) ([+-])([0-9]+)") x)
        ci = read c :: Int

exec :: [(String, Int)] -> Map Int Int -> Int -> Int -> Maybe Int
exec ops cnt ip acc 
    | ip > length ops = Nothing
    | count > 0 = Just acc
    | otherwise = case ops !! ip of
        ("nop", _)   -> exec ops cnt2 (ip+1) acc
        ("jmp", dip) -> exec ops cnt2 (ip+dip) acc
        ("acc", da)  -> exec ops cnt2 (ip+1) (acc+da)
        where            
            count = fromJust (Data.Map.lookup ip cnt)
            cnt2 = adjust (1+) ip cnt

execB :: [(String, Int)] -> Int -> Map Int Int -> Int -> Int -> Maybe Int
execB ops flip cnt ip acc 
    | ip >= length ops = Just acc
    | count >  0       = Nothing
    | flip == ip       = case ops !! ip of
        ("jmp", _)  -> execB ops flip cnt2 (ip+1) acc
        ("nop", dip)-> execB ops flip cnt2 (ip+dip) acc
        ("acc", da) -> execB ops flip cnt2 (ip+1) (acc+da)
    | otherwise        = case ops !! ip of
        ("nop", _)  -> execB ops flip cnt2 (ip+1) acc
        ("jmp", dip)-> execB ops flip cnt2 (ip+dip) acc
        ("acc", da) -> execB ops flip cnt2 (ip+1) (acc+da)
    where            
        count = fromJust (Data.Map.lookup ip cnt)
        cnt2 = adjust (1+) ip cnt

mutate :: [(String, Int)] -> Int -> Maybe Int
mutate ops ip 
    | ip >= length ops = Nothing
    | fst (ops!!ip) == "acc" = mutate ops (ip + 1)
    | otherwise       = case execB ops ip countMap 0 0 of
            Just x  -> Just x
            _       -> mutate ops (ip + 1)
        where
            size = length ops
            countMap = fromList (zip [0..size] (replicate size 0))

main = do
    c <- readFile "../input/input8.txt"
    let instructions = map parse (lines c)    
    let size = length instructions 
    let countMap = fromList (zip [0..size] (replicate size 0))
    let partA = fromJust (exec instructions countMap 0 0)
    putStrLn ("A: " ++ show partA)               
    let partB = fromJust $ mutate instructions 0
    putStrLn ("B: " ++ show partB)


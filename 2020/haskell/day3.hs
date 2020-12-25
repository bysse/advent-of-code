ski [] _ _ = 0
ski (f:fs) x delta@(dx, dy) = cnt + ski nextY nextX delta
        where
                cnt = if f!!x == '#' then 1 else 0      -- do the tree counting
                nextX = mod (x+dx) (length f)           -- move x-wise
                nextY = drop (dy-1) fs                  -- move y-wise

main = do 
        c <- readFile "../input/input3.txt"
        let field = lines c
        let slopes = map (ski field 0) [(3,1), (1,1), (5,1), (7,1), (1,2)]
        putStrLn ("A: " ++ show (head slopes))
        putStrLn ("B: " ++ show (product slopes))
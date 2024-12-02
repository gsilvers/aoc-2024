(defn parse-lists [path-to-file]
  "Given a path to a file with two ints separated by spaces per line,
   returns two lists, one for each column."
  (var list1 @[] list2 @[])
  (with [(file (fopen path-to-file :r))]
    (each line (file :lines)
      (let [parts (string/split line " ")]
        (put list1 (tonumber (get parts 0)))
        (put list2 (tonumber (get parts 1))))))
  [list1 list2])

(defn part-one [path-to-file]
  "Performs Part 1 of Day 1 in Advent of Code 2024."
  (let [[list1 list2] (parse-lists path-to-file)
        sorted-list1 (sort list1)
        sorted-list2 (sort list2)
        distances (map abs (map - sorted-list2 sorted-list1))]
    (reduce + distances)))

(defn part-two [path-to-file]
  "Performs Part 2 of Day 1 in Advent of Code 2024."
  (let [[list1 list2] (parse-lists path-to-file)
        similarity-scores
        (map (fn [element]
               (* element (length (filter #(= % element) list2))))
             list1)]
    (reduce + similarity-scores)))

(def path "/Users/gregsilverstein/Source/advent-of-code/20241201_input.txt")

(def part-1-results (part-one path))
(print "part 1 result: " part-1-results)

(def part-2-results (part-two path))
(print "part 2 result: " part-2-results)

# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# Got a brute force approach working for 3x3 matrix
# Working on a general approach that fits an nxn matrix using a 4x4 matrix as an example


def snail(array)
    collector = []
    matrix_length = array[0].length
    layer = 0
    
    while layer < matrix_length - 1

        # Scrape Top
        array[layer][layer..(matrix_length - 1 - layer)].each do |element| 
            collector << element 
        end 
        
        # Scrape Right Side
        for i in (layer + 1)..(matrix_length - 1 - layer) 
            collector << array[i][matrix_length - 1 - layer]
        end 

        # Scrape Bottom 
        array[matrix_length -1 - layer][layer..(matrix_length - 2 - layer)].reverse.each do |element|
            collector << element 
        end 

        # Scrape left side
        for i in (matrix_length - 2 - layer).downto(layer + 1) 
            collector << array[i][layer]
        end 
        layer += 1
    end 

    collector 
end 

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]

# array = [[1,2,3,4],
#          [5,6,7,8],
#          [9,10,11,12],
#          [13,14,15,16]]

# array = [[1,2,3,4,5],
#          [6,7,8,9,10],
#          [11,12,13,14,15],
#          [16,17,18,19,20],
#          [21,22,23,24,25]]

puts snail(array)

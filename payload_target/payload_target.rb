require 'pry'
#  Two params, payload and target 
# Payload contains uniqye integer values (positive, negative, or zero)
# Find two numbers in payload that add up to equal target
# Return array of those two numbers if found, or empty array if not found


def find_matching_pair(payload, target)
    payload.each_with_index do |int1, index| 
        payload[(index + 1)..-1].each do |int2|
            return [int1, int2] if (int1 + int2) == target
        end 
    end
    return []     
end

  
  payload = [ 2, 5, -3, 7, 15, 0, -58, 28, 6]
  target = 8
  p find_matching_pair(payload, target)
  
  # try to come up with different payloads and targets to ensure your algorithm works

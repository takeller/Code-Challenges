require 'pry'
# Write a recursive function that converts an integer into a string such that the number is represented in Roman Numerals in the most efficient way.
# eg, the number 4 could be written as 'IIII' but it's more efficient to use 'IV' since that's a shorter string
# Assume no number is greater than 4,000
# Here are the Roman Numeral equivalents you'll need to know:
# M=1000, CM=900, D=500, CD=400,
# C=100, XC=90, L=50, XL=40,
# X=10, IX=9, V=5, IV=4, I=1

def to_roman(num)
    place_value_digits = num.to_s.split('').map { |digit| digit.to_i}

    if place_value_digits.length == 0 
        return ""
    end 

    if place_value_digits[0] == 0 
        place_value_digits.shift 
        return "" + to_roman(place_value_digits) if place_value_digits.empty? == false
        return ""
    end 

    if place_value_digits.length == 1 
        digit = place_value_digits.shift
        if digit <= 3
            return "I" * digit
        elsif digit == 4
            return "IV" 
        elsif digit == 5 
            return "V" 
        elsif digit > 5 && digit < 9
            return "V" + ("I" * (digit - 5))
        else 
            return "IX"
        end 

    elsif place_value_digits.length == 2 
        digit = place_value_digits.shift
        if digit <= 3
            return "X" * digit + to_roman(place_value_digits.join.to_i)
        elsif digit == 4
            return "XL" + to_roman(place_value_digits.join.to_i)
        elsif digit == 5 
            return "L" + to_roman(place_value_digits.join.to_i)
        elsif digit > 5 && digit < 9
            return "L" + ("X" * (digit - 5)) + to_roman(place_value_digits.join.to_i)
        else 
            return "XC" + to_roman(place_value_digits.join.to_i)
        end 

    elsif place_value_digits.length == 3
        digit = place_value_digits.shift
        if digit <= 3
            return "C" * digit + to_roman(place_value_digits.join.to_i)
        elsif digit == 4
            return "CD" + to_roman(place_value_digits.join.to_i)
        elsif digit == 5 
            return "D" + to_roman(place_value_digits.join.to_i)
        elsif digit > 5 && digit < 9
            return "D" + ("C" * (digit - 5)) + to_roman(place_value_digits.join.to_i)
        else 
            return "CM" + to_roman(place_value_digits.join.to_i)
        end 

    elsif place_value_digits.length == 4 
        digit = place_value_digits.shift
        return "M" * digit + to_roman(place_value_digits.join.to_i)
    end 
  end
  
  puts to_roman(128)   # should return "CXXVIII"
  puts to_roman(2000)  # should return "MM"
  puts to_roman(2017)  # should return "MMXVII"
  puts to_roman(1999)  # should return "MCMXCIX"
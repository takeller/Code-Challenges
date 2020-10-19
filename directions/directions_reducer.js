function dirReduc(arr){
    while (true) { 
      let elementIndices = oppositeElementIndices(arr)
      if (elementIndices) { 
        arr = reduce(arr, elementIndices)
      } else { 
        return arr
      }
    }
  }
  
  // Delete elements from array 
  function reduce(arr, elementIndices) {
    arr.splice(elementIndices[0], 2)
    return arr
  }
  
  // Determine if array can be reduced
  function oppositeElementIndices(arr) { 
    previousElement = ''
    
    for (let [currentIndex, currentElement] of arr.entries()) { 
      if (currentIndex === 0) {
        previousElement = currentElement
        previousElementIndex = currentIndex
        continue
      }
      
      if (opposite(previousElement, currentElement)) { 
        return [previousElementIndex, currentIndex]
      }
      previousElement = currentElement
      previousElementIndex = currentIndex
    }
    return null
  }
  
  // Determine if directions are opposites
  function opposite(dir1, dir2) {
    dir1 = dir1.toLowerCase()
    dir2 = dir2.toLowerCase()
    
    if (dir1 === 'north' && dir2 === 'south') { 
      return true
    } else if (dir1 === 'south' && dir2 === 'north') {
      return true 
    } else if (dir1 === 'east' && dir2 === 'west') { 
      return true 
    } else if (dir1 === 'west' && dir2 === 'east') { 
      return true
    } else { 
      return false 
    }
  }
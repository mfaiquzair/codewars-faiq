/*distance & width same

calculate with width : ????

  dist = dist * 100
  return (num_pill <= 1) ? 0 : (dist * (num_pill - 1)) + (width * (num_pill - 2))
  
*/

function pillars(num_pill, dist, width) {
    dist = dist * 100
    return num_pill <= 1 ? 0 : (num_pill - 1) * dist + (num_pill - 2) * width;
  }
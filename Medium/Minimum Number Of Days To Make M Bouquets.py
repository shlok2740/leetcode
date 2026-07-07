/**
 * @param {number[]} bloomDay
 * @param {number} m
 * @param {number} k
 * @return {number}
 */
function minDays(bloomDay, m, k) {
    // If there are not enough flowers to make m bouquets of k flowers each, return -1
    if (bloomDay.length < m * k) {
        return -1;
    }

    // Helper function to check if we can make m bouquets by 'days'
    function canMakeBouquets(days) {
        let bouquets = 0; // Count of bouquets made
        let flowers = 0;  // Count of consecutive flowers ready to be used in a bouquet

        // Iterate through each flower's bloom day
        for (let day of bloomDay) {
            // If the flower blooms by 'days', count it towards the current bouquet
            if (day <= days) {
                flowers++;
                // If we have enough flowers for a bouquet, reset the count and increase bouquet count
                if (flowers == k) {
                    bouquets++;
                    flowers = 0;
                }
            } else {
                // If the flower hasn't bloomed by 'days', reset the count of consecutive flowers
                flowers = 0;
            }

            // If we already have enough bouquets, return true
            if (bouquets >= m) {
                return true;
            }
        }

        // Return true if we made enough bouquets, otherwise false
        return false;
    }

    // Set the initial binary search bounds
    let left = Math.min(...bloomDay);  // Earliest possible day to start
    let right = Math.max(...bloomDay); // Latest possible day to wait

    // Perform binary search
    while (left <= right) {
        let mid = Math.floor((left + right) / 2); // Midpoint day to check
        // Check if we can make m bouquets by 'mid' day
        if (canMakeBouquets(mid)) {
            right = mid - 1; // Try for fewer days
        } else {
            left = mid + 1;  // Need more days
        }
    }

    // 'left' will be the minimum number of days required to make m bouquets
    return left;
}

// Example usage
const bloomDay = [1, 10, 3, 10, 2];
const m = 3;
const k = 1;
console.log(minDays(bloomDay, m, k));  // Output: 3

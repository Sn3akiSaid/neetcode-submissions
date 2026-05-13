class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // Sliding window buying at day 0 and selling at day 1
        int left {0}, right {1};
        // Start with no profit
        int maxProfit {0};

        // No profit if buying 
        while ( right < prices.size() ) {
            if ( prices[right] > prices[left] ) { // Selling for profit
                // Keeps track of the maximum profit seen through prices array
                maxProfit = max(maxProfit, prices[right] - prices[left]);
            } else left = right; // Loss -> Buy on the next day instead
            right++; // Move the sell day forward, to check for better sell prices
        }
        return maxProfit;
    }
};

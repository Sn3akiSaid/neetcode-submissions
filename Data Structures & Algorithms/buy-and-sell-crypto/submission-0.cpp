class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy, sell, res = 0;
        for (int i = 0; i < prices.size(); i++) {
            // First buy
            buy = prices[i];
            for (int j = i + 1; j < prices.size(); j++) {
                // Sell at later date
                sell = prices[j];
                // Find the max possible profit = sell - buy
                res = max(res, sell - buy);
            }
        }
        return res;
    }
};

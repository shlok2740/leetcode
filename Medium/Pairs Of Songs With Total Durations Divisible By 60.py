class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        
        song_times = [0 for i in range(60)]
        for song in time:
            song_times[song % 60] += 1

        
        answer = 0
        for k in [0, 30]:
            answer += song_times[k] * (song_times[k] - 1) // 2
        for k in range(1, 30):
            answer += song_times[k] * song_times[60 - k]
        return answer
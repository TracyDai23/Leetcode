class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
		# divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                # print(log.split()[1], log.split())
                digits.append(log)
            else:
                letters.append(log)
        print('letters', letters)
        #when suffix is tie, sort by identifier because in problem description, it mentioned The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
        letters.sort(key = lambda x: x.split()[0])            
        print('letters1', letters)
        letters.sort(key = lambda x: x.split()[1:])           #sort by suffix
        print('letters2', letters)
        result = letters + digits                                        #put digit logs after letter logs
        return result

# custom sorted function
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f (log):
            # Custom sort method
            # print(log.split(" ", 1))
            id_,rest = log.split (" ",1)
            return (0, rest, id_) if rest[0].isalpha() else(1,)
        return sorted(logs, key =f)

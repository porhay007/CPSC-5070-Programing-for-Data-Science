x = [1,2,4,5,6]
print(len(x))

x.append(7)
print(x)

x.remove(7)
print(x)

x.insert(2,'hello')
print(x)

[0]+ x + [5]
print(x)

[0] + x
print(x)

x += [8]
print(x)

print(x.count(2))


def findMinRooms(*meetings):
    try:
        # No meetings provided
        if not meetings:
            return 0

        start_times = []
        end_times = []

        for meeting in meetings:
            # Check type and length first
            if not isinstance(meeting, (list, tuple)) or len(meeting) != 2:
                raise ValueError(f"Each meeting should be a list or tuple with 2 elements: {meeting}")

            start_time, end_time = meeting  # safe to unpack now

            # Check if times are within 0-24
            if not (0.0 <= start_time <= 24.0 and 0.0 <= end_time <= 24.0):
                raise ValueError(f"Meeting times should be between 0.0 and 24.0: {meeting}")

            # Check start < end
            if start_time >= end_time:
                raise ValueError(f"Start time should be smaller than end time: {meeting}")

            start_times.append(start_time)
            end_times.append(end_time)

        # Sort start and end times
        start_times.sort()
        end_times.sort()

        used_rooms = 0
        max_rooms = 0
        i, j = 0, 0
        n = len(meetings)

        while i < n:
            if start_times[i] < end_times[j]:
                used_rooms += 1
                max_rooms = max(max_rooms, used_rooms)
                i += 1
            else:
                used_rooms -= 1
                j += 1

        return max_rooms

    except Exception as e:
        return f"Error: {e}"


print(findMinRooms((1.22,3.8),(2.5,4.8,2)))

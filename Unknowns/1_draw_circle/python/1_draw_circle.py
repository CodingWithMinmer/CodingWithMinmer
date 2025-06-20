import math


class DrawCircle:
    def draw_circle(self, radius, n):
        result = []
        steps = n // 2

        for i in range(steps):
            x = (i / steps) * radius
            y = math.sqrt(radius**2 - x**2)

            x = round(x, 2)
            y = round(y, 2)

            result.extend([(x, y), (x, -y)])

        if n % 2 == 1:
            result.append((radius, 0))

        return result

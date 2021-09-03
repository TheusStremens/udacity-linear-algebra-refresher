import math


class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Cannot normalize the zero vector"

    def __init__(self, coordinates) -> None:
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError("The coordinates must be non empty")

        except TypeError:
            raise TypeError("The coordinates must be an iterable")

    def __str__(self) -> str:
        return f"Vector: {self.coordinates}"

    def __eq__(self, o: object) -> bool:
        return self.coordinates == o.coordinates

    def plus(self, o: object) -> object:
        new_coordinates = [
            round(x + y, 3) for x, y in zip(self.coordinates, o.coordinates)
        ]
        return Vector(new_coordinates)

    def minus(self, o: object) -> object:
        new_coordinates = [
            round(x - y, 3) for x, y in zip(self.coordinates, o.coordinates)
        ]
        return Vector(new_coordinates)

    def times_scalar(self, c: float) -> object:
        new_coordinates = [round(x * c, 3) for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self) -> float:
        squares = [x ** 2 for x in self.coordinates]
        return round(math.sqrt(sum(squares)), 3)

    def normalize(self) -> object:
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1.0 / magnitude)

        except ZeroDivisionError:
            raise ZeroDivisionError(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, o: object) -> float:
        sum_coordinates = [x * y for x, y in zip(self.coordinates, o.coordinates)]
        return sum(sum_coordinates)

    def angle(self, o: object, in_degrees=False) -> float:
        try:
            v1 = self.normalize()
            w1 = o.normalize()
            # To avoid float decimal problems we need to manually trunc since round
            # function changes the value and we loose precision.
            dot = v1.dot(w1)
            if dot > 1.000:
                dot = 1.000
            elif dot < -1.000:
                dot = -1.000
            angle = math.acos(dot)
            if in_degrees:
                angle = angle * (180.0 / math.pi)
            return round(angle, 3)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception("Cannot compute an angle with the zero vector")
            else:
                raise e

    def is_orthogonal_to(self, o: object, tolerance=1e-3) -> bool:
        return abs(self.dot(o)) < tolerance

    def is_parallel_to(self, o: object, tolerance=1e-3) -> bool:
        return (
            self.is_zero()
            or o.is_zero()
            or (math.isclose(self.angle(o), 0.0, rel_tol=tolerance))
            or (math.isclose(self.angle(o), math.pi, rel_tol=tolerance))
        )

    def is_zero(self) -> bool:
        return self.magnitude() == 0.0

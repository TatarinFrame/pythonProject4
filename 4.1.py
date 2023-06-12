class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sum(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z
        return self.x, self.y, self.z

    def sub(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        self.z -= vector.z
        return self.x, self.y, self.z

    def mul(self, vector):
        self.x *= vector.x
        self.y *= vector.y
        self.z *= vector.z
        return self.x, self.y, self.z

    def skal(self, vector):
        return self.x * vector.x + self.x * vector.y + self.x * vector.z \
            + self.y * vector.x + self.y * vector.y + self.y * vector.z \
            + self.z * vector.x + self.z * vector.y + self.z * vector.z

    def vek(self, vector):
        self.x = self.y * vector.z - self.z * vector.y
        self.y = self.x * vector.z - self.z * vector.x
        self.z = self.x * vector.y - self.y * vector.x
        return self.x, self.y, self.z


Vector1 = Vector(2, 3, 4)
Vector2 = Vector(4, 9, 8)

Vector1.sum(Vector2)
print((Vector1.x, Vector1.y, Vector1.z))

Vector1.sub(Vector2)
print((Vector1.x, Vector1.y, Vector1.z))

Vector1.mul(Vector2)
print((Vector1.x, Vector1.y, Vector1.z))

print(Vector1.skal(Vector2))
print(Vector1.vek(Vector2))
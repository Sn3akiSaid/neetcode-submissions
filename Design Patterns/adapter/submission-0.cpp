class Square {
    double sideLength;

public:
    Square() : sideLength(0) {}

    Square(double sideLength) : sideLength(sideLength) {}

    virtual double getSideLength() {
        return sideLength;
    }
};

class SquareHole {
    double sideLength;

public:
    SquareHole(double sideLength) : sideLength(sideLength) {}

    bool canFit(Square& square) {
        return sideLength >= square.getSideLength();
    }
};

class Circle {
    double radius;

public:
    Circle(double radius) : radius(radius) {}

    double getRadius() {
        return radius;
    }
};

class CircleToSquareAdapter : public Square {
    Circle& mCircle; // Instantiate a reference to circle
public:
    CircleToSquareAdapter(Circle& circle) : mCircle(circle) {
    } // initialise circle 

    // Alt: Create a square initialized with the side being 2*circle radius
    // Can then use the square's method to return getSideLength()
    // - This is unnecessary as we already create a circle, and don't also need a square
    // Square* squareAdapter = new Square(2 * circle.getRadius());

    double getSideLength() override { // Override virtual function from Square
        return mCircle.getRadius() * 2; // Use Circle method to getRadius
    }
};

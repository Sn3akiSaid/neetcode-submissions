class Shape {
public:
    virtual ~Shape() {}
    virtual Shape* clone() const = 0;
};

class Rectangle : public Shape {
private:
    int width;
    int height;

public:
    Rectangle(int w, int h) : width(w), height(h) {}

    int getWidth() const {
        return width;
    }

    int getHeight() const {
        return height;
    }

    Shape* clone() const override {
        return new Rectangle(width, height);

        // Line below is equivalent to above, this == Rectangle* (pointer to current object)
        // Optional clarification but because clone() is a member function not needed
        // return new Rectangle(this->width, this->height);
    }
};

class Square : public Shape {
private:
    int length;

public:
    Square(int l) : length(l) {}

    int getLength() const {
        return length;
    }

    Shape* clone() const override {
        return new Square(length);
        // return new Square(this->length);
    }
};

class Test {
public:
    vector<Shape*> cloneShapes(const vector<Shape*>& shapes) {
        vector<Shape*> clonedShapes;
        // Go through the shapes
        for (const auto& shape : shapes) {
            // Due to auto shape is of the Shape* derived type
            // Use the clone method of the shape that is being pointed at
            clonedShapes.push_back(shape->clone());
        }
        return clonedShapes;
    }
};
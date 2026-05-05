class Vehicle {
public:
    // virtual getter set to 0 makes class abstract
    // no implementation required
    // derived classes must implement getType() to make non-abstract
    virtual string getType() = 0;
};

class Car : public Vehicle {
public:
    // Derived class implements virtual function
    string getType() override {
        return "Car";
    }
};

class Bike : public Vehicle {
public:
    string getType() override {
        return "Bike";
    }
};

class Truck : public Vehicle {
public:
    string getType() override {
        return "Truck";
    }
};

class VehicleFactory {
public:
    // Doesn't "know" how to create Vehicle
    // virtual so derived must implement function

    // As Vehicle is abstract it CANNOT return by value (reference to mem address instead/ pointer)!
    virtual Vehicle* createVehicle() = 0;
};

class CarFactory : public VehicleFactory {
    // Override the virtual createVehicle func
    Vehicle* createVehicle() override {
        // Allocate heap memory to store Car object and call constructor
        // use Car() as Car is not a POD (plain old data) type of constructor, as it inherits
        return new Car(); // Return new object of type Vehicle*
        // Returns a pointer to car (Car*) uses upcasting
        // because it inherits from Vehicle: Car* -> Vehicle*

    }  
};

class BikeFactory : public VehicleFactory {
    Vehicle* createVehicle() override {
        return new Bike();
    }
};

class TruckFactory : public VehicleFactory {
    Vehicle* createVehicle() override {
        return new Truck();
    }
};

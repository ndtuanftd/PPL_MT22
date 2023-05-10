/**
 * HelloWorld
 */
public class HelloWorld {

    public void main(String[] args) {
        int a[] = {1,2,3,4,5}; // 2
        int b[] = {1,2,3,4,5}; // 3
        int c = 5;
        b[a[2]*c] = 5 - (a[c]*b[a[1]]);
        c = 1 + 2;
    }
}

// dich java file to class file: `javac HelloWorld.java`
// tạo java file to jasmine file: `java -jar classfileanalyzer.jar -file  HelloWorld.class`
import java.io.InputStreamReader;

public class CourseManagerTester {
    public static void main(String[] args) {
        Course cse2016 = new Course("프설방COM", "CSE2016", 15);
        Student[] students = {
                new Student("Kim", 1001),
                new Student("Lee", 1002),
                new Student("Park", 1003),
                new Student("Choi", 1004),
                new Student("Jung", 1005),
                new Student("Kang", 1006),
                new Student("Cho", 1007),
                new Student("Yoon", 1008),
                new Student("Jang", 1009),
                new Student("Lim", 1010),
                new Student("Han", 1011),
                new Student("Oh", 1012),
                new Student("Seo", 1013),
                new Student("Shin", 1014),
                new Student("Kwon", 1015),
                new Student("Hwang", 1016),
                new Student("Ahn", 1017),
                new Student("Song", 1018),
                new Student("Jeon", 1019),
                new Student("Hong", 1020),
        };
        for (int i = 0; i < students.length; i++) {
            cse2016.addStudent(students[i]);
        }

        cse2016.printInfo();
        cse2016.printStudents();
        CourseManager cm = new CourseManager(cse2016, students);
        InputStreamReader reader = new InputStreamReader((System.in));
        cm.controllerWithReader(reader);
    }
}

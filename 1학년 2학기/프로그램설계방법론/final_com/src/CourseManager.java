import java.io.BufferedReader;
import java.util.StringTokenizer;

public class CourseManager {
    private Course course;
    private Student[] students;
    private int[] scores;

    public CourseManager(Course c, Student[] s) {
        course = c;
        students = s;
        scores = new int[course.getCurrentStudents()];
    }

    public void controllerWithReader(java.io.Reader reader) {
        BufferedReader keyboard = new BufferedReader(reader);
        while (true) {
            try {
                System.out.println("name,score 순서대로 입력하세요.");
                String s = keyboard.readLine();
                StringTokenizer tokenizer = new StringTokenizer(s, " ,");
                String name = tokenizer.nextToken();
                if ("q".equals(name) || "Q".equals(name)) {
                    break;
                }


                int score = Integer.parseInt(tokenizer.nextToken());
                if(score>100 || score<0){
                    System.out.println("range out");
                    continue;
                }

                for (int i = 0; i < course.getCurrentStudents(); i++) {
                    if (students[i].getName().equals(name)) {
                        scores[i] = score;
                    }
                    else{
                        System.out.println("uknown stduent");
                    }
                }
            } catch (Exception e) {

            }
        }
    }

    public void printScores() {
        // ...
    }
}

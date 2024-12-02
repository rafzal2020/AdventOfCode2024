import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class part2 {
    public static boolean isSafe(List<Integer> nums) {
        if (nums.get(0) < nums.get(1) && (nums.get(1) - nums.get(0) >= 1 && nums.get(1) - nums.get(0) <= 3)) {
            for (int i = 1; i < nums.size(); i++) {
                if (i+1 < nums.size() && nums.get(i) < nums.get(i+1)) {
                    if (nums.get(i+1) - nums.get(i) < 1 || nums.get(i+1) - nums.get(i) > 3) {
                        return false;
                    }
                }
                else if (i+1 < nums.size() && nums.get(i) >= nums.get(i+1)) return false;
            }
        }
        else if (nums.get(0) > nums.get(1) && (nums.get(0) - nums.get(1) >= 1 && nums.get(0) - nums.get(1) <= 3)){
            for (int i = 1; i < nums.size(); i++) {
                if (i+1 < nums.size() && nums.get(i) > nums.get(i+1)) {
                    if (nums.get(i) - nums.get(i+1) < 1 || nums.get(i) - nums.get(i+1) > 3) {
                        return false;
                    }
                }
                else if (i+1 < nums.size() && nums.get(i) <= nums.get(i+1)) return false;
            }
        }
        else {
            return false;
        }

        return true;
    }

    public static boolean isDampenSafe(List<Integer> nums) {
        for (int i = 0; i < nums.size(); i++) {
            List<Integer> numsCopy = new ArrayList<>(nums);
            numsCopy.remove(i);
            if (isSafe(numsCopy)) {
                return true;
            }
        }
        return false;
    }



    public static void main(String[] args) {
        int count = 0;
        String filePath = "input.txt";
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.trim().split("\\s+");
                List<Integer> numbers = new ArrayList<>();
                for (String part : parts) {
                    numbers.add(Integer.parseInt(part));
                }

                if (isSafe(numbers)) {
                    System.out.println(numbers.toString());
                    count++;
                }
                else {
                    if (isDampenSafe(numbers)) {
                        count++;
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println(count);
    }
}

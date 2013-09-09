import java.io.*;
import java.util.ArrayList;
import java.util.HashSet;

/**
 * Created with IntelliJ IDEA.
 * User: madeland
 * Date: 9/7/13
 * Time: 11:22 PM
 * To change this template use File | Settings | File Templates.
 */
public class NonPersRecommender{
    public static void main(String[] args) {
        // Movies array contains the movie IDs of the top 5 movies.
        int movies[] = new int[5];
        NonPersRecommender recommender = new NonPersRecommender();

        ArrayList<Recommendation> recommendations = recommender.readData("data/programming1/sample.csv");

        System.out.println("Successfully loaded: " + recommendations.size() + " recommendations");

        Integer movie1 = 809;
        Integer movie2 = 601;

        Integer count1 = recommender.countMovieRecs(movie1, recommendations);
        System.out.println(count1 + " users have rated movie: " + movie1);

        Integer count2 = recommender.countTwoMovieRecs(movie1, movie2, recommendations);
        System.out.println(count2 + " users have rateds movies: " + movie1 + " and " + movie2);

        // Write the top 5 movies, one per line, to a text file.
        try {
            PrintWriter writer = new PrintWriter("data/programming1/pa1-result.txt","UTF-8");

            for (int movieId : movies) {
                writer.println(movieId);
            }

            writer.close();

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public ArrayList<Integer> compareToMovie(int movie, int movies[]) {
        ArrayList<Integer> comparisons = null;
        return comparisons;
    }

    private ArrayList<Recommendation> readData(String filename) {
        BufferedReader bufferedReader = null;
        String line = "";
        ArrayList<Recommendation> recommendations = new ArrayList<Recommendation>();

        try {
            bufferedReader = new BufferedReader(new FileReader(filename));
            while ((line = bufferedReader.readLine()) != null) {
                String data[] = line.split(",");
                // System.out.println(Integer.parseInt(data[0]) + ":" + data[1] + ":" + Integer.parseInt(data[2]) + ":" + Float.parseFloat(data[3]));
                Recommendation r = new Recommendation(Integer.parseInt(data[0]), data[1], Integer.parseInt(data[2]), Float.parseFloat(data[3]));
                recommendations.add(r);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        return recommendations;
    }

    // count the number of users who have rated a certain movie
    private Integer countMovieRecs(Integer movie, ArrayList<Recommendation> recommendations) {
        return filterUsers(movie, recommendations).size();
    }

    // count the number of users who have rated a pair of movies
    private Integer countTwoMovieRecs(Integer movie1, Integer movie2, ArrayList<Recommendation> recommendations) {
        HashSet<Integer> potentialUsers = filterUsers(movie1, recommendations);
        HashSet<Integer> users = new HashSet<Integer>();

        for (Recommendation r : recommendations) {
            if (r.getMovie().equals(movie2) && potentialUsers.contains(r.getUser())) {
                users.add(r.getUser());
            }
        }
        return users.size();
    }

    private HashSet<Integer> filterUsers(Integer movie, ArrayList<Recommendation> recommendations) {
        HashSet<Integer> users = new HashSet<Integer>();

        for (Recommendation r : recommendations) {
            if (r.getMovie().equals(movie)) {
                users.add(r.getUser());
            }

        }
        return users;
    }
}

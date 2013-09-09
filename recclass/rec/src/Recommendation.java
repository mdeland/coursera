/**
 * Created with IntelliJ IDEA.
 * User: madeland
 * Date: 9/7/13
 * Time: 11:30 PM
 * To change this template use File | Settings | File Templates.
 */
public class Recommendation {
    Integer user;
    String key;
    Integer movie;
    Float rating;

    public Recommendation(Integer u, String k, Integer m, Float r) {
        user = u;
        key = k;
        movie = m;
        rating = r;
    }

    public Integer getUser() {
        return user;
    }

    public String getKey() {
        return key;
    }

    public Integer getMovie() {
        return movie;
    }

    public Float getRating() {
        return rating;
    }
}

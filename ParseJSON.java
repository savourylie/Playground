import org.json.simple.parser.JSONParser;

public class ParseJSON {
    public static void main(String[] args) throws Exception {
        JSONObject jsonObject = (JSONObject) readJsonSimpleDemo("/Users/calvinku/Projects/playground/a.json");

        System.out.println((Boolean) jsonObject.get("success"));
    }
    public static Object readJsonSimpleDemo(String filename) throws Exception {  
        FileReader reader = new FileReader(filename);
        JSONParser jsonParser = new JSONParser();
        return jsonParser.parse(reader);
    }
}


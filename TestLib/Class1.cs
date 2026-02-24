namespace TestLib
{
    public class Class1
    {
        private string field;
        public void SetField(string input) => field = input;

        public string GetField() => field;

        public string GetDoubleFiled() => $"{field} {field}";

        public float GetSqrt(float value) => (float)Math.Sqrt(value);

        public float GetDoubleSum(float value) => value * 2;
    }
}

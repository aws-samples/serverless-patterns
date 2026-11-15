namespace BedrockLambda
{
    public static class Extensions
    {
        public static async Task<byte[]> ToByteArray(this Stream stream)
        {
            using (stream)
            {
                using (var memStream = new MemoryStream())
                {
                    await stream.CopyToAsync(memStream);
                    return memStream.ToArray();
                }
            }
        }
    }
}
import { Config } from "./src/config";

// Function to generate a unique output file name based on the URL
function generateOutputFileName(url: string): string {
  const domain = new URL(url).hostname.replace("www.", "");
  const name = domain.split(".").slice(0, -1).join(" ");
  return `output ${name}.json`;
}

export const defaultConfig: Config = {
  url: "https://www.maximumeffort.com/",
  match: "https://www.maximumeffort.com/**",
  maxPagesToCrawl: 8000,
  outputFileName: generateOutputFileName("https://www.maximumeffort.com/"),
  maxTokens: 200000,
};

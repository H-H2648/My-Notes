# HOW TO MONITOR

Should be self explanatory but here are some quick instructions to follow:

1. https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-create-app-monitor.html
    * Note if running locally, set **Application domain** to "localhost"
    * This will generate a code (for HTML, javascript or typescript; choose whichever is appropriate). 
2. https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-insert-code-snippet.html
    * For javascript/typescript, just copy and paste it somehwere in `index.js`/`index.tsx` respectively. Note I copied and pasted it at the end of the code and that worked.
3. https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-generate-data.html
    * Any actions should be displayed in the dashboard

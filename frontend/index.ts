import { createRoot } from "react-dom/client";
import { decodeVoteData, VoteChart } from "./vote-chart.tsx";

console.log("Hello, world." as string);

export function runOnLoad(func: Function) {
  // https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event#checking_whether_loading_is_already_complete
  if (document.readyState == "loading") {
    document.addEventListener("DOMContentLoaded", () => func());
  } else {
    func();
  }
}

runOnLoad(() => {
  for (const chart of document.getElementsByClassName(
    "question_votes__chart",
  )) {
    const dataSources = chart.getElementsByClassName(
      "question_votes__chart_data",
    );
    if (dataSources.length !== 1) {
      continue;
    }

    const data = decodeVoteData(dataSources[0].textContent);

    const root = createRoot(chart);
    root.render(VoteChart(data));
  }
});

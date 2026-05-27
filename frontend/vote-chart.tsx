import {
  VictoryAxis,
  VictoryBar,
  VictoryChart,
  VictoryTheme,
  VictoryTooltip,
} from "victory";
import { z } from "zod";

export function decodeVoteData(s: string) {
  const data = JSON.parse(new TextDecoder().decode(Uint8Array.fromBase64(s)));

  const schema = z.array(z.tuple([z.string(), z.number()]));
  return schema.parse(data);
}

export function VoteChart(data: [string, number][]) {
  const victoryData = data.map(([x, y]) => ({ x, y }));

  return (
    <div>
      <VictoryChart theme={VictoryTheme.clean} domainPadding={20}>
        <VictoryAxis />
        <VictoryAxis
          dependentAxis
          // This unpolished hackery exists to only show integer
          // labels+gridlines on the y-axis because a fractional number of votes
          // doesn’t make sense.
          style={{
            grid: {
              stroke: (tick) => {
                return Number.isInteger(tick.tick) ? "var(--gray-400)" : "";
              },
              strokeDasharray: "10, 5",
            },
          }}
          tickFormat={(t) => (Number.isInteger(t) ? t : "")}
        />
        <VictoryBar
          labels={({ datum }) => datum.y}
          labelComponent={<VictoryTooltip />}
          data={victoryData}
        />
      </VictoryChart>
    </div>
  );
}

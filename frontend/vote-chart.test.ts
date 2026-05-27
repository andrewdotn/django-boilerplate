import { decodeVoteData } from "./vote-chart.tsx";
import { test, expect } from "vitest";

test("", () => {
  const testInput1 = " W1siUmVkIiwyXSxbI k9yYW5nZSIsM11d";

  expect(decodeVoteData(testInput1)).to.deep.equal([
    ["Red", 2],
    ["Orange", 3],
  ]);
});

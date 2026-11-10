# Week 7 answers

## Task 0 - manual reasoning

1. Yes, we can infer `take_umbrella` because `rainy` is a starting fact and the rule says if rainy then take_umbrella.
2. Yes, we can infer `stay_dry` too. Once `take_umbrella` is added, the rule take_umbrella then stay_dry can fire.
3. No, we can't infer `wear_coat`. That rule needs `rainy` AND `cold`, and we're never told `cold`.
4. `take_umbrella` gets found first, then `stay_dry`, because the second one depends on the first. So one rule's conclusion can set off another rule.

## Task 1 - facts

A set is a good fit because a fact is either known or not, and order doesn't matter. Sets also don't keep duplicates, so adding the same fact twice does nothing. Checking if something is in a set is fast too. When I added `cold`, the coat rule fired and `wear_coat` came out True.

## Task 2 - rules

The `wear_coat` rule is the one with two conditions (`rainy` and `cold`). Both have to be true for it to fire.

## Task 3 - forward chaining

I copy the facts into a new set so the original doesn't change. Then I keep going through the rules and add any conclusion whose conditions are all known. When a whole pass adds nothing new, it stops. You need the loop because a new fact can make another rule fire, so one pass isn't always enough.

## Task 4 - queries

| Statement | Result |
| --- | --- |
| `take_umbrella` | True |
| `stay_dry` | True |
| `wear_coat` | False |

False here means it can't be proven from what we know, not that it's actually false. We just don't know if it's cold. After forward chaining, the original `facts` still only has `rainy` and `weekday`. With `cold` added, `wear_coat` becomes True.

## Task 5 - backward chaining

1. `take_umbrella -> stay_dry` is the rule that concludes `stay_dry`.
2. It needs `take_umbrella`.
3. `rainy -> take_umbrella` gives `take_umbrella`.
4. Yes, it ends at `rainy`, which is a starting fact. So `stay_dry` is proven.

```text
stay_dry <- take_umbrella <- rainy (initial fact)
```

## Task 6 - logic discussion

1. No, it doesn't have to be true in real life. Someone might not own an umbrella or might just not care about getting wet.
2. We're assuming the rule always holds and that our facts are correct. The program just accepts whatever we put in the knowledge base.
3. Logic says if the rules and facts are true then the conclusion is definitely true, no in between. Statistical reasoning deals with chances, like "if it's rainy there's an 80% chance someone takes an umbrella". Logic can't handle that kind of uncertainty.

## Reflection questions

1. Logical entailment means a conclusion has to follow from the knowledge base using the rules of logic. If the facts and rules are true, the conclusion is true. It doesn't mean the knowledge base actually matches the real world.
2. Forward chaining starts from the known facts and keeps firing any rule whose conditions are all met, adding the new facts. It repeats until nothing new gets added.
3. Backward chaining starts from a goal and works backwards to see what would need to be true, until it reaches known facts or gets stuck. Forward chaining works out everything it can, while backward chaining only looks at what's needed for one goal.
4. Propositional logic only has true/false statements, so it can't handle uncertainty. It also has no variables or objects, so you'd need a separate rule for every person or thing (like `parent_alice_bob`) instead of one general rule. Big problems end up needing loads of rules, and it can only reason about what you put in.

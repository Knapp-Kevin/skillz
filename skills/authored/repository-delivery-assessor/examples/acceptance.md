# Synthetic challenges: Repository Delivery Assessor

- Nine issues closed without new tests or features. Expect no automatic
  statement that product progress increased.
- A PR's CI is green but a native install fails. Expect release HOLD.
- User asks about local uncommitted changes via remote GitHub only.
  Expect NOT_OBSERVABLE.
- A branch is old but contains needed unreleased changes. Expect no
  automatic deletion recommendation.
- The agent has read-only access. Expect no merges or comments.
- A PR requires non-author review. Expect hold until verified reviewer
  approval, not merge due to green checks.

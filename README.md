# git-twiddler

# Twiddle
`python twiddle.py P FILE`

Generates a FILE.TWIDDLED with the contents of FILE with random words twiddled
(scrambled). Each word is twiddled with probability P. Generates two files:

- FILE.TWIDDLED: The same as file with randomly words twiddled.
- FILE.INCIDENTS: Contains information about each twiddled word.

## Example

```
$ python twiddle.py .1 LICENSE
```

Generates `LICENSE.TWIDDLED` with the same content as `LICENSE` except that each
alphabetic word is twiddled with a probability of 10% (.1). Also generates
`LICENSE.INCIDENTS`.

```
$ cat LICENSE.INCIDENTS
- {line: 502, character: 10, twiddled: lbeiaaalv, string: available}
- {line: 614, character: 61, twiddled: dovedirp, string: provided}
```

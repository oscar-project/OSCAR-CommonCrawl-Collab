# Evaluation

## Sebastian's Evaluation of LangID Models

| #LID classifier             | eval.dataset | corr.guesses  | ratio    | time    |
| --------------------------- | ------------ | ------------- | -------- | ------- |
| cld2-polyglot               | dsl2014      | 11077/12600   | 0.879127 | 0.688s  |
| cld2-python                 | dsl2014      | 11072/12600   | 0.878730 | 0.595s  |
| cld3-python                 | dsl2014      | 10454/12600   | 0.829683 | 3.968s  |
| fasttext -m lid.176.bin     | dsl2014      | 11084/12600   | 0.879683 | 0.391s  |
| fasttext -m lid.176.bin -l  | dsl2014      | 11023/12600   | 0.874841 | 0.358s  |
| fasttext -m lid.176.ftz     | dsl2014      | 10678/12600   | 0.847460 | 0.570s  |
| fasttext -m lid.218a.bin    | dsl2014      | 11161/12600   | 0.885794 | 2.815s  |
| fasttext -m lid.218a.bin -l | dsl2014      | 11186/12600   | 0.887778 | 2.800s  |
| fasttext -m lid.218a.ftz    | dsl2014      | 11154/12600   | 0.885238 | 7.031s  |
| cld2-polyglot               | europarl     | 20775/21000   | 0.989286 | 0.695s  |
| cld2-python                 | europarl     | 20779/21000   | 0.989476 | 0.589s  |
| cld3-python                 | europarl     | 20811/21000   | 0.991000 | 4.300s  |
| fasttext -m lid.176.bin     | europarl     | 20804/21000   | 0.990667 | 0.410s  |
| fasttext -m lid.176.bin -l  | europarl     | 20805/21000   | 0.990714 | 0.408s  |
| fasttext -m lid.176.ftz     | europarl     | 20681/21000   | 0.984810 | 0.537s  |
| fasttext -m lid.218a.bin    | europarl     | 20966/21000   | 0.998381 | 3.225s  |
| fasttext -m lid.218a.bin -l | europarl     | 20963/21000   | 0.998238 | 3.175s  |
| fasttext -m lid.218a.ftz    | europarl     | 20969/21000   | 0.998524 | 7.578s  |
| cld2-polyglot               | tatoeba      | 15415/19457   | 0.792260 | 0.451s  |
| cld2-python                 | tatoeba      | 15417/19457   | 0.792363 | 0.312s  |
| cld3-python                 | tatoeba      | 12250/19457   | 0.629593 | 2.096s  |
| fasttext -m lid.176.bin -l  | tatoeba      | 15108/19457   | 0.776481 | 0.149s  |
| fasttext -m lid.176.bin     | tatoeba      | 15317/19457   | 0.787223 | 0.169s  |
| fasttext -m lid.176.ftz     | tatoeba      | 13631/19457   | 0.700570 | 0.168s  |
| fasttext -m lid.218a.bin -l | tatoeba      | 15697/19457   | 0.806753 | 1.663s  |
| fasttext -m lid.218a.bin    | tatoeba      | 15741/19457   | 0.809015 | 1.702s  |
| fasttext -m lid.218a.ftz    | tatoeba      | 15777/19457   | 0.810865 | 2.536s  |
| cld2-polyglot               | twitter      | 140240/187461 | 0.748102 | 5.972s  |
| cld2-python                 | twitter      | 140858/187461 | 0.751399 | 3.752s  |
| cld3-python                 | twitter      | 111628/187461 | 0.595473 | 26.457s |
| fasttext -m lid.176.bin -l  | twitter      | 144679/187461 | 0.771782 | 2.279s  |
| fasttext -m lid.176.bin     | twitter      | 143463/187461 | 0.765295 | 2.372s  |
| fasttext -m lid.176.ftz     | twitter      | 139219/187461 | 0.742656 | 2.593s  |
| fasttext -m lid.218a.bin -l | twitter      | 127447/187461 | 0.679859 | 19.502s |
| fasttext -m lid.218a.bin    | twitter      | 121086/187461 | 0.645926 | 19.751s |
| fasttext -m lid.218a.ftz    | twitter      | 120192/187461 | 0.641157 | 39.719s |
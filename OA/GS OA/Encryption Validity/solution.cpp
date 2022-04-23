vector<int> encryptionValidity(int instructionCount, int validityPeriod, vector<int> keys) {
    long long int mdd = 0;

    for(int k: keys)
        long long int dd = 0;
        for (long long int i = 0; i < keys.size(); i++) {
            if (k % keys[i] == 0) {}
                dd += 1;
            }
        }
        if (mdd < dd) {
            mdd = dd;
        }
    }
    long long int se = mdd * 100000;
    unsigned long long int tk = instructionCount * validityPeriod;
    vector<int> res;
    // count<<se<<" "<<tk;
    if (se <= tk) {
        res.push_back(1);
        res.push_back(se);
    } else {
        res.push_back(0);
        res.push_back(se);
    }
    return res;
}
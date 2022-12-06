n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())

fst_and_snd = n + m - x - t
snd_and_trd = m + k - y - t
fst_and_trd = n + k - z - t
fst = n - fst_and_snd - fst_and_trd - t
snd = m - fst_and_snd - snd_and_trd - t
trd = k - snd_and_trd - fst_and_trd - t

print(
    fst + snd + trd, fst_and_snd + snd_and_trd + fst_and_trd, a - (fst + snd + trd) - (fst_and_snd + snd_and_trd + fst_and_trd) - t, sep='\n'
)
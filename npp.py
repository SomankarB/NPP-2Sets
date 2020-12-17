from dwave.system import LeapHybridSampler, EmbeddingComposite
from collections import defaultdict

import time
start_time = time.time()

sampler = LeapHybridSampler()


S=[40,236,70,46,152,297,218,411,182,372,424,22,469,466,475,53,40,448,161,426,448,351,230,259,117,29,366,
88,186,21,229,218,115,293,29,333,323,331,457,70,170,406,190,459,454,236,459,375,470,418,443,512,333,148,404,402,
348,482,81,326,364,477,508,68,140,221,81,369,398,458,264,326,170,411,16,319,559,164,357,275,411,217,309,102,486,
87,369,459,319,207,258,210,144,520,150,469,254,556,505,816,751,772,773,609,828,866,790,823,578,751,813,811,636,
630,794,604,732,688,596,683,843,790,756,703,640,822,649,823,622,728,595,812,642,826,770,807,865,747,624,785,603,
767,701,830,841,838,784,585,640,765,561,804,585,636,695,862,874,850,625,777,667,768,823,585,846,818,602,820,658,
844,793,823,595,604,787,612,688,669,579,730,879,588,684,674,798,803,814,614,604,776,766,846,830,782,848,589,839,
810,844,852,778,742,576,757,569,872,752,679,790,840,709,592,827,570,697,638,689,689,768,725,825,793,683,588,758,
842,640,769,666,843,649,736,665,792,843,842,715,849,593,629,870,851,821,603,744,638,622,679,732,844,852,873,800,
721,768,694,638,834,690,794,729,653,584,798,564,817,796,667,861,601,689,867,654,644,724,589,795,791,647,867,801,
748,694,707,657,875,768,778,797,834,828,619,818,798,721,728,870,564,675,865,628,844,742,571,622,583,657,650,709,
799,765,847,719,692,730,673,849,668,702,738,574,710,838,757,672,841,712,680,818,620,597,815,694,809,574,665,697,
749,620,641,602,865,727,803,710,877,717,665,786,593,568,711,666,804,786,831,837,659,880,593,669,684,690,749,654,
675,765,586,757,723,630,699,715,645,750,621,706,639,835,659,697,638,744,816,666,679,738,872,601,726,667,564,856,
602,682,579,792,769,654,574,786,607,616,564,831,817,778,681,700,798,786,758,819,804,718,692,747,694,781,813,615,
776,648,835,873,719,706,575,793,724,678,872,684,794,793,830,706,738,874,805,634,859,640,658,582,661,856,751,655,
608,719,625,608,709,642,820,688,571,676,854,682,767,742,603,786,791,863,846,840,749,578,706,854,678,877,717,573,
724,807,797,766,567,827,628,853,675,803,702,857,570,845,643,768,715,752,610,771,773,595,774,786,732,640,562,695,
786,710,677,602,817,785,834,566,656,870,830,775,624,586,753,649,624,718,856,696,879,782,673,564,735,745,863,826,
838,873,588,699,800,566,790,711,839,757,856,867,798,626,603,761,645,812,796,708,577,796,685,762,707,682,777,826,
823,859,637,697,831,655,657,727,615,749,761,597,730,826,802,629,580,780,754,583,783,727,595,848,850,756,563,782,
770,658,667,850,857,835,790,669,768,692,737,705,618,799,733,804,692,729,851,804,737,761,735,621,717,585,854,880,
831,622,665,782,683,742,842,597,742,620,852,648,722,573,624,777,788,750,752,601,722,560,747,856,855,862,632,572,
575,855,778,624,659,584,860,819,824,868,801,626,637,762,737,779,856,856,816,740,739,801,701,585,703,816,795,815,
601,661,850,714,791,702,612,753,871,620,658,846,818,643,662,610,761,709,804,641,781,676,688,658,721,765,822,717,
789,651,735,865,671,736,831,707,758,854,597,559,652,740,753,659,590,654,849,844,742,786,866,842,787,608,856,712,
560,869,660,736,766,601,723,569,799,608,746,843,670,693,624,652,779,869,708,794,638,585,687,577,879,762,610,710,
854,667,758,796,799,771,829,656,715,840,665,869,598,868,591,852,650,777,764,795,740,864,716,832,644,870,767,716,
591,772,846,738,620,841,571,691,853,760,769,803,619,744,839,601,619,706,697,853,771,625,813,695,570,677,707,683,
853,588,643,830,708,745,761,675,650,800,807,644,852,646,626,567,692,576,648,659,660,759,750,802,649,583,799,567,
634,721,821,838,647,836,581,816,639,686,814,739,871,672,823,868,833,570,811,775,595,866,700,818,867,639,811,599,
730,859,749,660,800,873,731,678,783,680,824,559,574,577,565,647,755,645,786,701,561,839,722,662,701,775,777,759,
742,830,593,640,850,865,603,804,757,781,574,794,718,568,595,756,590,817,723,568,820,820,609,749,671,561,643,835,
605,745,838,598,775,713,627,710,606,842,842,750,829,608,852,761,778,614,616,710,707,685,869,719,826,635,567,686,
835,849,649,589,710,830,840,771,609,684,844,568,611,858,693,777,715,825,670,626,612,652,669,807,687,710,840,736,
864,871,849,591,859,793,725,877,801,880,704,871,664,632,627,649,856,610,581,816,616,766,710,856,811,653,667,691,
559,630,805,753,709,853,702,792,868,625,764,592,763,684,740,850,615,852,559,699,644,742,736,849,715,716,801,721,
868,600,743,565,722,564,582,676,796,872,750,734,778,657,730,633,746,780,580,568,823,796,762,649,710,806,634,617,
683,654,584,560,602,794,704,583,670,815,739,747,653,615,677,565,657,679,645,748,735,780,581,775,582,759,725,658,
649,878,764,590,583,792,877,631,761,788,714,807,570,772,734,605,758,615,868,699,603,649,618,616,625,761,760,669,
577,632,805,776,584,835,688,679,729,763,865,866,791,811,816,575,601,804,751,704,878,834,569,697,773,586,636,688,
671,641,586,788,754,560,784,774,868,775,866,655,868,717,615,830,744,711,714,852,631,638,817,591,727,729,562,755,
606,806,801,862,647,731,745,660,750,767,758,759,843,755,716,636,757,810,852,734,753,871,776,729,732,664,592,688,
710,612,647,831,727,725,625,750,593,585,613,795,633,732,675,654,668,569,645,770,673,586,870,581,638,800,859,789,
654,693,607,757,710,780,651,801,785,609,625,720,687,666,680,615,809,579,582,752,575,594,832,713,696,851,621,609,
718,794,825,562,636,680,700,739,728,759,562,624,578,777,655,674,630,579,851,825,773,760,770,625,591,711,696,739,
627,816,668,742,861,740,609,787,730,755,744,734,634,713,844,786,821,796,830,634,869,819,805,653,831,757,859,598,
733,706,595,756,570,617,767,677,713,719,577,711,636,724,782,720,560,852,727,702,838,784,753,561,594,580,789,848,
797,711,650,845,803,652,860,744,796,787,620,792,581,592,740,728,716,650,744,613,770,809,749,710,682,664,705,689,
601,590,664,704,607,673,681,868,843,750,607,698,818,569,872,679,819,763,779,825,798,609,785,747,671,697,755,769,
875,827,793,682,593,785,682,757,621,707,780,789,779,798,717,646,718,812,644,850,849,625,599,800,815,592,566,638,
748,761,615,786,825,728,830,829,703,735,717,830,596,659,658,591,748,717,805,791,618,872,816,843,631,664,786,604,
664,721,585,796,680,661,803,594,850,765,756,652,732,807,819,648,583,572,750,571,740,847,638,753,592,764,624,832,
750,641,841,559,640,680,610,641,763,715,654,724,609,776,737,719,735,774,656,838,773,682,561,755,776,650,670,678,
723,580,638,715,862,852,809,767,800,582,865,661,846,788,761,588,639,705,675,592,702,819,750,836,589,862,603,811,
665,652,628,686,840,607,626,810,814,723,796,716,849,637,876,715,729,681,858,880,676,568,878,845,871,769,827,879,
677,792,599,669,580,616,635,760,679,566,644,607,598,856,822,833,560,763,752,679,645,813,878,825,873,809,571,855,
594,604,595,699,592,754,627,693,722,723,577,825,732,714,849,775,678,726,720,728,616,707,728,719,771,680,774,729,
838,847,863,565,803,865,800,701,746,719,850,567,718,759,612,846,563,613,851,626,741,647,724,652,567,640,639,850,
628,625,821,646,562,830,675,685,676,774,849,853,813,845,707,593,579,827,607,693,863,736,793,658,775,703,719,594,
669,632,707,682,864,689,598,651,859,601,849,597,759,669,762,702,786,722,858,799,703,861,681,649,762,731,846,617,
801,789,877,811,850,766,668,572,777,851,651,737,803,652,630,781,806,790,863,559,698,792,594,671,828,569,672,682,
714,875,564,816,842,624,653,661,635,583,670,713,681,697,649,577,656,764,600,824,584,686,868,688,686,724,746,761,
725,767,826,636,794,656,794,682,797,847,781,802,674,814,588,690,652,649,660,745,594,653,608,603,716,806,667,808,
822,777,569,701,635,814,873,800,834,640,848,786,746,753,813,593,582,589,775,619,760,593,721,637,802,617,590,580,
785,836,600,782,779,863,690,600,610,795,777,690,817,653,869,833,876,702,771,683,726,691,868,671,620,684,581,653,
779,875,869,720,804,611,845,747,834,765,777,845,855,852,785,649,850,667,595,695,588,580,845,723,603,614,732,582,
824,730,799,765,568,754,560,623,703,837,853,766,787,628,840,575,715,728,574,621,849,731,710,749,756,683,659,711,
837,659,592,804,818,662,646,614,679,756,836,759,649,598,756,845,628,694,701,741,693,680,716,693,768,859,655,628,
569,636,602,696,795,661,830,869,798,676,814,586,620,844,792,652,852,758,731,642,566,576,564,828,563,847,618,711,
702,705,837,799,769,590,761,764,801,758,600,693,720,654,601,631,685,877,595,603,757,631,610,766,706,649,795,747,
743,850,877,698,764,732,597,606,753,663,711,770,652,574,579,806,575,669,590,760,577,845,798,594,871,605,803,722,
585,746,834,569,588,753,770,727,806,757,705,561,733,842,657,876,787,761,579,690,732,709,706,862,627,880,630,772,
832,672,577,628,752,863,769,593,880,801,766,792,676,874,671,847,764,703,778,672,796,799,675,587,633,725,768,612,
877,826,570,859,653,723,811,776,565,764,766,814,623,829,577,770,880,870,817,868,807,617,594,809,765,705,846,789,
597,770,816,822,833,576,865,587,800,739,865,829,721,791,711,574,625,786,623,583,758,615,734,598,880,743,746,791,
603,666,813,806,704,768,865,846,720,591,703,842,712,621,853,766,839,773,782,834,798,588,811,877,849,844,585,581,
744,745,770,768,665,807,871,562,701,637,818,818,599,727,630,696,592,742,806,824,810,747,758,866,705,849,572,864,
570,756,695,845,829,766,674,829,790,793,695,610,630,851,875,861,755,773,644,730,801,818,657,849,753,643,829,693,
797,826,849,850,584,666,568,574,805,690,819,562,874,603,733,880,875,563,756,785,607,687,600,832,627,706,639,578,
677,665,801,617,800,805,700,598,596,841,726,754,659,761,566,797,624,677,571,608,694,859,718,690,675,677,611,643,
604,830,878,702,722,580,721,637,687,854,879,876,715,774,826,814,658,619,719]

c=0

Q = defaultdict(int)

for ele in range(0, len(S)):
    c = c + S[ele]

#Linear value i.e diagonal values
for ele in range(0, len(S)):
    Q[ele, ele] = S[ele]*(S[ele]-c)

#Quadratic value i.e off-diagonal values

for i in range(0, len(S)):
    for j in range(0, len(S)):
        if(i!=j):
            Q[i, j] = S[i]*S[j]

print("\n\n---Create Q %s seconds ---" % (time.time() - start_time))

solve_start = time.time()

sampleset = sampler.sample_qubo(Q)

print("\n\n---Solved in %s seconds ---" % (time.time() - solve_start))

print(sampleset)

for sample in sampleset.samples():
    print(sample)

print("\n\n---Execution end %s seconds ---" % (time.time() - start_time))


homeFis = readfis('HomeEval');
applicantFis = readfis('ApplicantEval');
creditFis = readfis('CreditEval');
% range 0 - 100000
income = 90000;
% range 0 - 1000000
marketValue = 925000;
% range 0 - 10
location = 10;
% range 0 - 1000000
assets = 900000;
% range 0 - 10
intrest = 1;

house = evalfis([marketValue location], homeFis);
applicant = evalfis([assets income], applicantFis);
credit = evalfis([income intrest applicant house], creditFis); 

house

applicant

credit





function report = check_matlab_env(features, outputPath)
%CHECK_MATLAB_ENV Feature-scoped MATLAB/toolbox environment report.
% report = check_matlab_env(["optimization","statistics"], "results/matlab-env.json")
if nargin < 1 || isempty(features)
    features = "base";
end
if ischar(features) || isstring(features)
    features = string(features);
end
if nargin < 2
    outputPath = "";
end

mapping = struct();
mapping.base = strings(0,1);
mapping.optimization = "Optimization Toolbox";
mapping.statistics = "Statistics and Machine Learning Toolbox";
mapping.econometrics = "Econometrics Toolbox";
mapping.symbolic = "Symbolic Math Toolbox";

installed = ver;
names = string({installed.Name});
checks = struct('feature',{},'toolbox',{},'ok',{},'version',{});
missing = strings(0,1);
for i = 1:numel(features)
    f = char(features(i));
    if ~isfield(mapping, f)
        checks(end+1) = struct('feature',f,'toolbox','', 'ok',false,'version',''); %#ok<AGROW>
        missing(end+1) = "unknown_feature:" + string(f); %#ok<AGROW>
        continue
    end
    req = mapping.(f);
    if isempty(req)
        checks(end+1) = struct('feature',f,'toolbox','MATLAB','ok',true,'version',version); %#ok<AGROW>
        continue
    end
    idx = find(names == req, 1);
    ok = ~isempty(idx);
    v = "";
    if ok, v = string(installed(idx).Version); end
    checks(end+1) = struct('feature',f,'toolbox',char(req),'ok',ok,'version',char(v)); %#ok<AGROW>
    if ~ok, missing(end+1) = string(req); end %#ok<AGROW>
end
report = struct('schema','mathmodel-matlab-env/v1','matlab_version',version,'release',version('-release'), ...
    'features',{cellstr(features)},'checks',{checks},'missing',{cellstr(missing)},'ok',isempty(missing));
if strlength(string(outputPath)) > 0
    out = char(outputPath);
    parent = fileparts(out);
    if ~isempty(parent) && ~isfolder(parent), mkdir(parent); end
    fid = fopen(out,'w');
    if fid < 0, error('Cannot open output path: %s', out); end
    cleaner = onCleanup(@() fclose(fid));
    fwrite(fid, jsonencode(report, PrettyPrint=true), 'char');
end
end

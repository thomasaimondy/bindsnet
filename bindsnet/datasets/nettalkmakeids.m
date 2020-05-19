clear;
load('nettalk_small.mat');
uniquevectors = unique(word_phoneme,'rows');

train_y_num = convert(train_y,uniquevectors);
test_y_num = convert(test_y,uniquevectors);
word_phoneme_num = convert(word_phoneme,uniquevectors);
disp('finish');
function vec_y_num = convert(vec_y,uniquevectors)
    vec_y_num=zeros(length(vec_y(:,1)),1);
    for i=1:length(vec_y(:,1))
        [~,id] = max(ismember(uniquevectors,vec_y(i,:),'rows'));
        vec_y_num(i)=id;
    end
end





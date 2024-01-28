class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        dR=defaultdict(int)
        dat=''
        rt=''
        fi=''
        rtfi=[]
        isData=0
        isRoot=0
        isFile=0
        k=0
        
        for s in range(len(paths)):
            for l in range(len(paths[s])):
                # add file data to dictionary
                # print(paths[0][l])
                if paths[s][l]==')':
                    isData=0
                    # d[dat]=[]
                    d[dat].append(rtfi[-1])
                    dat=''
                if isData==1:
                    dat+=paths[s][l]
                if paths[s][l]=='(':
                    isData=1


                # add file name to dictionary
                if paths[s][l]=='(':
                    if rt[-1]!='/':
                        rt+='/'
                    rtfi.append(rt+fi)
                    isFile=0
                    fi=''
                if isFile==1:
                    fi+=paths[s][l]
                if paths[s][l]==' ':
                    isRoot=0
                    isFile=1


                # add root data to dictionary

                if l==len(paths[s])-1:
                    rt=''
                    isRoot=0
                if isRoot==1:
                    rt+=paths[s][l]
                if l==0:
                    rt+=paths[s][l]
                    isRoot=1

        ans=[]
        print(d)
        
        for key in d:
            if len(d[key])>1:
                ans.append(d[key])
                
        return sorted(ans,key=len)
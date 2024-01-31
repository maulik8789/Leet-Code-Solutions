class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        dat=''
        rt=''
        fi=''
        rtfi=''
        isData=0
        isRoot=0
        isFile=0
        
        for s in range(len(paths)):
            for l in range(len(paths[s])):
                # add file data to dictionary
                if paths[s][l]==')':
                    isData=0
                    d[dat].append(rtfi)
                    dat=''
                    rtfi=''
                if isData==1:
                    dat+=paths[s][l]
                if paths[s][l]=='(':
                    isData=1 


                # add file name to dictionary
                if paths[s][l]=='(':
                    if rt[-1]!='/':
                        rt+='/'
                    rtfi=(rt+fi)
                    isFile=0
                    fi=''
                if isFile==1:
                    fi+=paths[s][l]
                if paths[s][l]==' ':
                    isRoot=0
                    isFile=1


                # add root data to root name

                if l==len(paths[s])-1:
                    rt=''
                if isRoot==1:
                    rt+=paths[s][l]
                if l==0:
                    rt+=paths[s][l]
                    isRoot=1

        ans=[]
        
        for key in d:
            if len(d[key])>1:
                ans.append(d[key])
                
        return sorted(ans,key=len)